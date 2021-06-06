import {UPDATE_POSTS, UPDATE_CATEGORIES} from "../mutation-types";

export default {
    state: () => ({
        posts: {},
        categories: [],
    }),
    getters: {
        categoryList(state) {
            return state.categories
        },
        postList(state) {
            return state.posts.results;
        },
        getPreviousURL(state) {
            return state.posts.previous;
        },
        getNextURL(state) {
            return state.posts.next;
        },
        hasPrevious(state) {
            return state.posts.current_page==2?true:!!state.posts.previous
        },
        hasNext(state) {
            return !!state.posts.next;
        },
        postRangeFirst(state) {
            return state.posts.range_first;
        },
        postRangeLast(state) {
            return state.posts.range_last;
        },
        postCurrentPageNumber(state) {
            return state.posts.current_page;
        },
        postCount(state) {
            return state.posts.count;
        },
    },
    mutations: {
        [UPDATE_CATEGORIES](state, payload) {
            state.categories = payload
        },
        [UPDATE_POSTS](state, payload) {
            state.posts = payload;
        },
    },
    actions: {
        [UPDATE_CATEGORIES]({commit}, payload) {
            commit(UPDATE_CATEGORIES, payload)
        },
        [UPDATE_POSTS]({commit}, payload) {
            commit(UPDATE_POSTS, payload);
        },
    },
}
