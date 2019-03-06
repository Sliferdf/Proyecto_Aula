<!--Código correspondiente a la creación de los elementos que se encontraran en la página-->
<template>
    <div id="app">
        <h1>Bienvenido : {{user}}</h1>

        <v-app id="inspire">
            <legend>Agregar Coworking</legend>
            <form>
                <!--Se crea el campo del Nombre del Coworking y se captura la infomación en el formato V-model-->
                <v-text-field
                v-model="name"
                label="Nombre"
                ></v-text-field>

                <!--Se crea el campo de la dirección del Coworking y se captura la información-->
                <v-text-field
                v-model="address"
                label="Direccion"
                ></v-text-field>

                <!--Se crea el campo de texto para indicar el porecio y se guarda la infoamción-->
                <v-text-field
                v-model="price"
                label="Precio"
                ></v-text-field>
            
               <!--Creacion del campo de texto de la calificación del Coworking y ademas se captura la información  de la calificación que el usuario ingresa-->
                <v-select
                v-model="calification"
                :items="items"
                label="Calificacion"
                ></v-select>

                <!--Se crea el boton para guardar la iformación completa del coworking-->
                <v-btn color="info">Guardar</v-btn>

                <!--Se  crea el boton para cancelar y borrar toda la información ingresada-->
                <v-btn disabled= true>Cancelar</v-btn>

            </form>
        </v-app>
    </div>
</template>

<!--Modelo para el retorno de los datos guardados, los métodos y todos los códigos correspondientes a JavaScript-->
<script>
export default { 
    data() {
        return {
            user: 'ROOT',
            name: '',
            address: '',
            price: '',
            calification: '',
            items : [
                1,2,3,4,5
            ]
        }
    },    
}
</script>

<!--Codigo que se encarga del estilo de la página-->
<style>

</style>

