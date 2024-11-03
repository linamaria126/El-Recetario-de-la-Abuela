import axios from 'axios';

export const getAllrecipies = () => {
    return axios.get("http://127.0.0.1:8000/api/recetas/")
}