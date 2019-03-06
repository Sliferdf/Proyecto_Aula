<!--Código correspondiente a la creación de los elementos que se encontraran en la página-->
<template>
  <div class="hello">
    <v-app>
      <!--Se creea la barra de herraminetas que el usario manejara-->
      <v-toolbar dark color="primary">
      <v-toolbar-side-icon></v-toolbar-side-icon>

      <!--Se crea el título de la barra de hheramientas, con un icono -->
      <v-toolbar-title class="white--text">Shared Office
        <v-icon>share</v-icon>
      </v-toolbar-title>

      <!--Se crea un espacio para que los siguientes elementos esten en la parte contraria-->
      <v-spacer></v-spacer>

      <!--Se crean varios icononos que estarán en la barra de tareas-->
      <v-btn icon>
        <v-icon>Catalog</v-icon>
      </v-btn>
  
      <v-btn icon>
        <v-icon>apps</v-icon>
      </v-btn>
  
      <v-btn icon>
        <v-icon>person</v-icon>
      </v-btn>
    </v-toolbar>


    <h1>{{ msg }}</h1>
    <h2>Coworkings List</h2>

    <!--Se crea una tabla donde se muestra la infomación de los Coworkings que se han guardado con sus correspondiente información-->
    <v-data-table
    :headers="headers"
    :items="coworks"
    class="elevation-1"
    >
    <!--Se pasa toda la información que se debe mostrar al usuario-->
    <template v-slot:items="props">
      <td>{{props.item.nombre}}</td>
      <td class="text-xs-right">{{ props.item.nombre }}</td>
      <td class="text-xs-right">{{ props.item.direccion }}</td>
      <td class="text-xs-right">{{ props.item.precio }}</td>
      <td class="text-xs-right">{{ props.item.calificacion }}</td>
    </template>
    </v-data-table>
    </v-app>
  </div>
</template>

<!--Modelo para el retorno de los datos guardados, métodos. Todos los códigos correspondientes a JavaScript-->
<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Coworking Catalog',
      headers: [{
        text: 'Nombre',
        align: 'left',
        sortable: false,
        value: 'nombre'
        },
        {text: 'Nombre', value: 'nombre'},
        {text: 'Direccion', value: 'direccion'},
        {text: 'Precio', value: 'precio'},
        {text: 'Calificacion', value: 'calificacion'},
        ],
        coworks : [
          {
            nombre: 'Konkafe',
            direccion: 'Poblado',
            precio: '200000',
            calificacion: 5
          },
          {
            nombre: 'SoloPola',
            direccion: 'Envigado',  
            precio: '300000',
            calificacion: 4.5
  
          }
        ]
    }
  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

h1, h2 { 
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
