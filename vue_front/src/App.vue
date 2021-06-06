<template>
    <div id="app" class="min-h-screen flex flex-col">
        <Header />
        <main class="flex-grow">
            <router-view v-show=!isLoading />
            <Loading v-show=isLoading />
        </main>
        <Footer />
    </div>
</template>

<script>
import {mapGetters} from 'vuex'
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
import Loading from "@/components/Loading.vue";

export default {
    components: {
        Header,
        Footer,
        Loading
    },
    computed: {
        ...mapGetters(['isLoading']),
    },
};
</script>

<style></style>
