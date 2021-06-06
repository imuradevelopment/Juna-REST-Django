<template>
    <main class="container">
        <p id="lead">{{postCount}}件中 {{postRangeFirst}}~{{postRangeLast}}件を一覧表示</p>
        <section>
            <router-link :to="{name: 'posts', params: {id: post.id}}" v-for="post of postList" :key="post.id" class="post">
                <article>
                    <figure>
                        <img :src="post.thumbnail" :alt="post.title" class="thumbnail">
                    </figure>
                    <p class="post-category" :style="{'color': post.category.color}">{{post.category.name}}</p>
                    <h2 class="post-title">{{post.title}}</h2>
                    <p class="post-lead">{{post.lead_text}}</p>
                </article>
            </router-link>
        </section>
        <hr class="divider">
        <nav id="page">
            <router-link class="h-6 w-6" v-if="hasPrevious" :to="getPostPreviousURL()" id="back"><img src="@/assets/back.png"></router-link>
            <span>Page {{postCurrentPageNumber}}</span>
            <router-link class="h-6 w-6" v-if="hasNext" :to="getPostNextURL()" id="next"><img src="@/assets/next.png"></router-link>
        </nav>
    </main>
</template>

<script>
// @ is an alias to /src
import {mapGetters, mapActions} from 'vuex'
import {UPDATE_POSTS, UPDATE_DISPLAYSTATUS} from '@/store/mutation-types';
import {RepositoryFactory} from '@/repository/repositoryFactory';
const PostsRepository = RepositoryFactory.get('posts')

export default {
    name: 'PostList',
    computed: {
        ...mapGetters(['postList', 'getPreviousURL', 'getNextURL', 'hasPrevious', 'hasNext', 'postRangeFirst', 'postRangeLast', 'postCurrentPageNumber', 'postCount', 'isLoading']),
    },
    watch: {
        '$route'() {
            this.getPosts()
        }
    },
    methods: {
        ...mapActions([UPDATE_POSTS, UPDATE_DISPLAYSTATUS]),
        async getPosts(inputParams=''){
            const params = this.$route.query
            const queryString = '?' + Object.keys(params).map(key => key + '=' + params[key]).join('&')
            const {data} = await PostsRepository.get((inputParams==null||queryString=='?' ? '' : queryString))
            // this.updateLoadStatus(false)
            this[UPDATE_POSTS](data)
        },
        updateLoadStatus(status){
            this[UPDATE_DISPLAYSTATUS](status)
        },
        async sleep(msec) {
            return new Promise(function(resolve) {
                setTimeout(function() {resolve()}, msec);
            })
        },
        getPostPreviousURL() {
            const url = new URL(this.getPreviousURL)
            const keyword = url.searchParams.get('keyword') || ''
            const category = url.searchParams.get('category') || ''
            const page = url.searchParams.get('page') || 1
            return this.$router.resolve({
                name: 'PostList',
                query: {keyword, category, page}
            }).route.fullPath
        },
        getPostNextURL() {
            const url = new URL(this.getNextURL)
            const keyword = url.searchParams.get('keyword') || ''
            const category = url.searchParams.get('category') || ''
            const page = url.searchParams.get('page')
            return this.$router.resolve({
                name: 'PostList',
                query: {keyword, category, page}
            }).route.fullPath
        }
    },
    created() {
        this.getPosts()
    },
};
</script>

<style scoped>
.home {
    @apply hover:text-red-900;
}
</style>
