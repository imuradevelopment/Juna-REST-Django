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
            <a class="h-6 w-6" v-if="hasPrevious" @click="getPostPrevious" id="back"><img src="@/assets/back.png"></a>
            <span>Page {{postCurrentPageNumber}}</span>
            <a class="h-6 w-6" v-if="hasNext" @click="getPostNext" id="next"><img src="@/assets/next.png"></a>
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
    methods: {
        ...mapActions([UPDATE_POSTS, UPDATE_DISPLAYSTATUS]),
        async getPosts(params=''){
            await this.sleep(5000)
            const {data} = await PostsRepository.get((params==null ? '' : params))
            this.updateLoadStatus(false)
            this[UPDATE_POSTS](data)
        },
        getPostPrevious() {
            this.getPosts(this.getPreviousURL)
        },
        getPostNext() {
            this.getPosts(this.getNextURL)
        },
        updateLoadStatus(status){
            this[UPDATE_DISPLAYSTATUS](status)
        },
        async sleep(msec) {
            return new Promise(function(resolve) {
                setTimeout(function() {resolve()}, msec);
            })
        }
    },
    created() {
        this.updateLoadStatus(true)
        this.getPosts()
    }
};
</script>

<style scoped>
.home {
    @apply hover:text-red-900;
}
</style>
