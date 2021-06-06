import PostsRepository from '@/repository/posts/postsRepository';
import CategoriesRepository from '@/repository/posts/CategoriesRepository';

const repositories = {
    posts: PostsRepository,
    categories: CategoriesRepository,
}

export const RepositoryFactory = {
    get: name => repositories[name]
};