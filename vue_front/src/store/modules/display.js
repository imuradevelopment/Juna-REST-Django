import {UPDATE_DISPLAYSTATUS} from "../mutation-types";

export default {
    state: () => ({
        display:{
            isLoading:false,
        },
    }),
    getters: {
        isLoading(state){
            return state.display.isLoading;
        }
    },
    mutations: {
        [UPDATE_DISPLAYSTATUS](state, payload) {
            state.display.isLoading = payload;
        },
    },
    actions: {
        [UPDATE_DISPLAYSTATUS]({commit}, payload) {
            commit(UPDATE_DISPLAYSTATUS, payload);
        },
    },
}
