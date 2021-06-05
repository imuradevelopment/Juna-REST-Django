import axios from 'axios' //追記

const baseDomain = 'http://127.0.0.1:8000';
const baseURL = `${baseDomain}/blog/api`;

export default axios.create({
    baseURL
})