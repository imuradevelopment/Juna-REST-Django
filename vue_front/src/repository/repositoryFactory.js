import PostsRepository from '@/repository/posts/postsRepository';

const repositories = {
    posts: PostsRepository,
}

export const RepositoryFactory = {
    get: name => repositories[name]
};