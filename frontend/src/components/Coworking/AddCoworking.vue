<!--Codigo correspondiente a la creacion de los elementos que se encontraran en la pagina-->
<template>
    <div id="app">
        <h1>Bienvenido : {{user}}</h1>

        <v-app id="inspire">
            <legend>Agregar Coworking</legend>
            <form>
                <!--Se crea el campo del Nombre del Coworking y se captura la infomacion en el formato V-model-->
                <v-text-field
                v-model="name"
                label="Nombre"
                ></v-text-field>

                <!--Se crea el campo de la direccion del Coworking y se captura la informacion-->
                <v-text-field
                v-model="address"
                label="Direccion"
                ></v-text-field>

                <!--Se crea el campo de texto para indicar el porecio y se guarda la infoamcion-->
                <v-text-field
                v-model="price"
                label="Precio"
                ></v-text-field>
            
               <!--Creacion del campo de texto de la calificacion del Coworking y ademas se captura la informacion  de la califoicacion que el usuario ingresa-->
                <v-select
                v-model="calification"
                :items="items"
                label="Calificacion"
                ></v-select>

                <!--Se crea el boton para guardar la iformacion completa del coworking-->
                <v-btn color="info">Guardar</v-btn>

                <!--Se  crea el boton para cancelar y borrar toda la informacion ingresada-->
                <v-btn disabled= true>Cancelar</v-btn>

            </form>
        </v-app>
    </div>
</template>

<!--Modelo para el retorno de los datos guardados y todos los codigos correspondientes a JavaScript-->
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

<!--Codigo que se encarga del estilo de la pagina-->
<style>

</style>

