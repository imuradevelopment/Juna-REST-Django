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

export default {
    name: "PostList",
    data() {
        return {
            postList: [],
        }
    },
    mounted() {
        this.$http(this.$httpPosts)
            .then(response => {
                return response.json()
            })
            .then(data => {
                this.postList = data
            })
    }
};
</script>

<style scoped>
.home {
    @apply hover:text-red-900;
}
</style>
