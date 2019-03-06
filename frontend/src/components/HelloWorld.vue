<template>
  <div class="hello">
    <v-app>
      <v-toolbar flat color="primary">
      <v-toolbar-side-icon></v-toolbar-side-icon>
  
      <v-toolbar-title class="white--text">Shared Office
        <v-icon>share</v-icon>
      </v-toolbar-title>
  
      <v-spacer></v-spacer>
  
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
    <v-toolbar flat color="white">
      <v-toolbar-title>Coworkings</v-toolbar-title>
      <v-divider
      class="mx-2"
      inset
      vertical
      ></v-divider>
      <v-spacer></v-spacer>

    <v-dialog v-model="dialog" max-width="500px">
      <template v-slot:activator="{on}">
        <v-btn id="new"  round color="primary" dark v-on="on">New Coworking</v-btn>
      </template>

      <v-card>
        <v-card-title>
          <span class="headline">Editar</span>
        </v-card-title>

        <v-card-text>
          <v-container grid-list-md>
            <v-layout wrap>

              <v-flex xs12 sm6 md4>
                <v-text-field label="Nombre"></v-text-field>
              </v-flex>

              <v-flex xs12 sm6 md4>
                <v-text-field label="Direccion"></v-text-field>
              </v-flex>

              <v-flex xs12 sm6 md4>
                <v-text-field label="Precio"></v-text-field>
              </v-flex>

              <v-flex xs12 sm6 md4>
                <v-text-field label="Calificacion"></v-text-field>
              </v-flex>
            <v-combobox
            v-model="chips"
            label="Servicios prestados"
            chips
            clearable
            prepend-icon="fiter_list"
            solo
            multiple
            >
              <template v-slot:section="data">
                <v-chip
                :selected="data.selected"
                close
                @input="remove(data.item)"
                >
                <strong> {{data.item}}</strong>&nbsp;
                </v-chip>
              </template>
            </v-combobox>

            </v-layout>
          </v-container>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" flat>Cancel</v-btn>
          <v-btn color="blue darken-1" flat>Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    </v-toolbar>

    <v-data-table
    :headers="headers"
    :items="coworks"
    class="elevation-1"
    dark="true"
    >
    <template v-slot:items="props" >
      <td>{{props.item.nombre}}</td>
      <td class="text-xs-right">{{ props.item.nombre }}</td>
      <td class="text-xs-right">{{ props.item.direccion }}</td>
      <td class="text-xs-right">{{ props.item.precio }}</td>
      <td class="text-xs-right">{{ props.item.calificacion }}</td>
      <v-icon
      small 
      class="mr-2">edit</v-icon>

      <v-icon
      small 
      class="mr-2">delete</v-icon>

        <v-icon
        small
        class="mr-2">more</v-icon>


    </template>
    </v-data-table>
    </v-app>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Coworking Catalog',
      chips: ['Conferencias', 'Cafe', 'Sofá'],
      dialog: false,

      headers: [{
        text: 'Nombre',
        align: 'left',
        sortable: false,
        value: 'nombre',
        },
        {text: 'Nombre', value: 'nombre'},
        {text: 'Direccion', value: 'direccion'},
        {text: 'Precio', value: 'precio'},
        {text: 'Calificacion', value: 'calificacion'},
        {text:'Accciones', value: 'acciones'}
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
  },
  methods: {
    remove(item){
      this.chips.splice(this.chips.indexOf(item), 1)
      this.chips = [...this.chips]

    }

  },
  computed: {
    formTitle(){
        return this.editedText === -1 ? 'New coworking' : 'Edit Coworking'
      }
  },

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
