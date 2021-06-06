import Repository from '@/repository/repository';

const categoriesResource = '/categories';

export default {
    get(params=''){
        return Repository.get(`${categoriesResource}${params}`);
    },
    getCategory(postId){
        return Repository.get(`${categoriesResource}/${postId}`);
    },
    createCategory(payload){
        return Repository.post(`${categoriesResource}`, payload);
    }
}