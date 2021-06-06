<template>
    <article class="container" v-if="post">
        <nav id="back"><a @click="goBack" title="前ページへ戻る"><img src="@/assets/back.png"></a></nav>
        <p class="post-category" :style="{'color': post.category.color}">{{post.category.name}}</p>
        <h1 class="post-title">{{post.title}}</h1>
        <p class="post-lead">{{post.lead_text}}</p>
        <hr class="divider">
        <div class="post-main">{{ post.main_text }}</div>
        <hr class="divider">
        <nav id="top"><a @click="scrollTop" title="一番上まで戻る"><img src="@/assets/ue.png"></a></nav>
    </article>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'
import {UPDATE_DISPLAYSTATUS} from "@/store/mutation-types";
import {RepositoryFactory} from '@/repository/repositoryFactory';
const PostsRepository = RepositoryFactory.get('posts')

export default {
    name: 'Post',
    props: {
        id: {type: Number},
    },
    data() {
        return {
            post: {},
            hasBefore: false,
        }
    },
    beforeRouteEnter(to, from, next) {
        next(component => {
            if (from.name) {
                component.hasBefore = true
            }
        })
    },
    computed: {
        ...mapGetters(['isLoading']),
    },
    created() {
        this[UPDATE_DISPLAYSTATUS](true)
        this.getPost()
    },
    methods: {
        ...mapActions([UPDATE_DISPLAYSTATUS]),
        async getPost(){

            const {data} = await PostsRepository.getPost(this.id)
            this.post = data
            this[UPDATE_DISPLAYSTATUS](false)
        },
        scrollTop() {
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        },
        goBack() {
            if (this.hasBefore) {
                this.$router.go(-1)
            } else {
                this.$router.push({name: 'posts'})
            }
        },
    }
}
</script>