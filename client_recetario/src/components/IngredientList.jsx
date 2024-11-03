import { useEffect, useState } from "react";
import { getAllingredients } from "../api/ingredients.api";


export function IngredientList() {
    const [ingredients, setIngredients] = useState([]);

    useEffect(()=>{
        async function loadIngredients(){
            const res = await getAllingredients();
            console.log(res);
            setIngredients(res.data);
            }
            loadIngredients();
    },[]);


    return(
        <div>
            {ingredients.map(ingredient => (
                <div>
                    <h1>{ingredient.nombre_ingrediente}</h1>
                    
                </div>
            ))}

        </div>
    )
}