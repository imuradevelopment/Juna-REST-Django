import Vue from "vue";
import Vuex from "vuex";
import posts from './modules/posts';
import display from './modules/display';

Vue.use(Vuex);

export default new Vuex.Store({
    strict: true,
    state: {},
    getters: {},
    mutations: {},
    actions: {},
    modules: {
        posts,
        display,
    },
});
