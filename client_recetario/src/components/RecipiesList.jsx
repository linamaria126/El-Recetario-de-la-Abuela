import { useEffect, useState } from "react";
import { getAllrecipies } from "../api/recipies.api";


export function RecipiesList(){
    const [recetas, setRecetas] = useState([]);

    useEffect(()=>{
        async function loadRecetas(){
            const res = await getAllrecipies();
            console.log(res);
            setRecetas(res.data);
            }
            loadRecetas();
    },[]);


    return(
        <div>
            {recetas.map(receta => (
                <div key={receta.id_recetas}>
                    <h1>{receta.nombre_receta}</h1>
                    <p>{receta.descripcion}</p>
                </div>
            ))}

        </div>
    )
}