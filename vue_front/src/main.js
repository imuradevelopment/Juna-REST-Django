import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "@/assets/tailwind.css"; //追加
import axios from 'axios' //追記
import VueAxios from 'vue-axios' //追記

Vue.config.productionTip = false;

Vue.use(VueAxios, axios) //追記

// Vue.prototype.$http = (url, opts) => fetch(url, opts);
// Vue.prototype.$httpPosts = "http://127.0.0.1:8000/blog/api/posts/";
Vue.prototype.$httpCategories = "http://127.0.0.1:8000/blog/api/categories/";

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
