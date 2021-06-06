<template>
    <header>
        <h1>
            <router-link :to="{name: 'posts'}">ブログ</router-link>
        </h1>
        <div id="form">
            <input type="text" placeholder="Search" class="text" v-model="keyword" @change="search">
            <div class="selectWrap">
                <select class="select" v-model="selected" @change="search">
                    <option value="" :key="-1">Category</option>
                    <option v-for="category of categoryList" :value="category.id" :key="category.id">{{category.name}}
                    </option>
                </select>
            </div>
        </div>
    </header>
</template>
<script>
import {mapActions, mapGetters} from 'vuex'
import {UPDATE_CATEGORIES, UPDATE_POSTS} from "@/store/mutation-types"
import {RepositoryFactory} from '@/repository/repositoryFactory';
const PostsRepository = RepositoryFactory.get('posts')
const CategoriesRepository = RepositoryFactory.get('categories')

    export default {
        name: 'search-bar',
        data() {
            return {
                keyword: this.$route.query.keyword || '',
                selected: this.$route.query.category || '',
            }
        },
        watch: {
            '$route'() {
                this.keyword = this.$route.query.keyword || ''
                this.selected = this.$route.query.category || ''
            }
        },
        created() {
            this.getCategories()
        },
        computed: {
            ...mapGetters(['categoryList'])
        },
        methods: {
            ...mapActions([UPDATE_CATEGORIES, UPDATE_POSTS]),
            search() {
                this.$router.push({name: 'PostList', query: {page: 1, keyword: this.keyword, category: this.selected}})
            },
            async getCategories(params=''){
                const {data} = await CategoriesRepository.get((params==null ? '' : params))
                this[UPDATE_CATEGORIES](data)
            },
            async getPosts(params=''){
                const {data} = await PostsRepository.get((params==null ? '' : params))
                this[UPDATE_POSTS](data)
            },
        }
    }
</script>