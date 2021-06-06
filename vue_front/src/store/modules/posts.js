import {UPDATE_POSTS} from "../mutation-types";

export default {
    state: () => ({
        posts: {},
    }),
    getters: {
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
        [UPDATE_POSTS](state, payload) {
            state.posts = payload;
        },
    },
    actions: {
        [UPDATE_POSTS]({commit}, payload) {
            commit(UPDATE_POSTS, payload);
        },
    },
}
