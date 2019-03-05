<template>
    <div id="app">
        <h1>Bienvenido : {{user}}</h1>

        <v-app id="inspire">
            <legend>Agregar Coworking</legend>
            <form>
                <v-text-field
                v-model="name"
                label="Nombre"
                ></v-text-field>

                <v-text-field
                v-model="address"
                label="Direccion"
                ></v-text-field>

                <v-text-field
                v-model="price"
                label="Precio"
                ></v-text-field>

                <v-select
                v-model="calification"
                :items="items"
                label="Calificacion"
                ></v-select>

                <v-btn color="info">Guardar</v-btn>

                <v-btn disabled= true>Cancelar</v-btn>

            </form>
        </v-app>
    </div>
</template>

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


<style>

</style>

