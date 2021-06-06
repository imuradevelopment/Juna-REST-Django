import Repository from '@/repository/repository';

const postsResource = '/posts';
// const detailResource = '/detail';

export default {
    get(params=''){
        return Repository.get(`${postsResource}${params}`);
    },
    getPost(postId){
        console.log(`${postsResource}/${postId}`);
        return Repository.get(`${postsResource}/${postId}`);
    },
    createPost(payload){
        return Repository.post(`${postsResource}`, payload);
    }
}