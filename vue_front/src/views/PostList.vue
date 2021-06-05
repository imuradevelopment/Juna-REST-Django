<template>
    <section class="container">
        <article class="post" v-for="post of postList" :key="post.id">
            <figure>
                <img :src="post.thumbnail" :alt="post.title" class="thumbnail">
            </figure>
            <p class="post-category" :style="{'color': post.category.color}">{{post.category.name}}</p>
            <h2 class="post-title">{{post.title}}</h2>
            <p class="post-lead">{{post.lead_text}}</p>
        </article>
    </section>
</template>

<script>
// @ is an alias to /src
import {mapGetters, mapActions} from 'vuex'
import {UPDATE_POSTS} from "@/store/mutation-types";
import {RepositoryFactory} from '@/repository/repositoryFactory';
const PostsRepository = RepositoryFactory.get('posts')

export default {
    name: 'PostList',
    computed: {
        ...mapGetters(['postList'])
    },
    methods: {
        ...mapActions([UPDATE_POSTS]),
        async fetch(){
            this.isLoading = true
            const {data} = await PostsRepository.get()
            this.isLoading = false
            this.posts = data;
            this[UPDATE_POSTS](data)
        }
    },
    created() {
        this.fetch()
    }
};
</script>

<style scoped>
.home {
    @apply hover:text-red-900;
}
</style>
