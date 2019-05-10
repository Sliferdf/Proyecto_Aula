<!--Código correspondiente a la creación de los elementos que se encontraran en la página-->
<template>
  <div class="hello">
    <v-app>
      <!--Se creea la barra de herraminetas que el usario manejara-->
      <v-toolbar dark color="primary" fixed="true">
        <v-toolbar-side-icon></v-toolbar-side-icon>

        <!--Se crea el título de la barra de hheramientas, con un icono -->
        <v-toolbar-title class="white--text">
          Shared Office
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

        <v-btn icon to="/login">
          <v-icon>person</v-icon>
        </v-btn>
      </v-toolbar>

      <h1>{{ msg }}</h1>
      <h2>Coworkings List</h2>
      <v-toolbar flat color="white">
        <v-toolbar-title>Coworkings</v-toolbar-title>
        <v-divider class="mx-2" inset vertical></v-divider>
        <v-spacer></v-spacer>

        <v-dialog v-model="dialog" max-width="500px">
          <template v-slot:activator="{on}">
            <v-btn id="new" round color="primary" dark v-on="on">New Coworking</v-btn>
          </template>

          <v-card>
            <v-card-title>
              <span class="headline">Editar</span>
            </v-card-title>

            <v-card-text>
              <v-container grid-list-md>
                <v-layout wrap>
                  <v-flex xs12 sm6 md4>
                    <v-text-field
                      v-model="cards.nombre"
                      :rules="[rules.required, rules.counter]"
                      label="Nombre"
                      counter
                      maxlength="30"
                    ></v-text-field>
                  </v-flex>

                  <v-flex xs12 sm6 md4>
                    <v-text-field
                      v-model="cards.direccion"
                      :rules="[rules.required]"
                      label="Direccion"
                    ></v-text-field>
                  </v-flex>

                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="cards.precio" :rules="[rules.required]" label="Precio"></v-text-field>
                  </v-flex>

                  <v-flex xs12 sm6 md4>
                    <v-text-field
                      v-model="cards.calificacion"
                      :rules="[rules.required]"
                      label="Calificacion"
                    ></v-text-field>
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
                      <v-chip :selected="data.selected" close @input="remove(data.item)">
                        <strong>{{data.item}}</strong>&nbsp;
                      </v-chip>
                    </template>
                  </v-combobox>
                </v-layout>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" flat>Cancel</v-btn>
              <v-btn color="blue darken-1" flat @click="postCoworking">Save</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>

      <!--Se crea una tabla donde se muestra la infomación de los Coworkings que se han guardado con sus correspondiente información-->
      <v-data-table :headers="headers" :items="coworks" class="elevation-1" dark="true">
        <!--Se pasa toda la información que se debe mostrar al usuario-->
        <template v-slot:items="props">
          <td class="text-xs-right">{{ props.item.nombre }}</td>
          <td class="text-xs-right">{{ props.item.direccion }}</td>
          <td class="text-xs-right">{{ props.item.precio }}</td>
          <td class="text-xs-right">{{ props.item.calificacion }}</td>
          <v-icon small class="mr-2">edit</v-icon>

          <v-icon small class="mr-2">delete</v-icon>

          <v-icon small class="mr-2">more</v-icon>
        </template>
      </v-data-table>
    </v-app>
  </div>
</template>

<!--Modelo para el retorno de los datos guardados, métodos. Todos los códigos correspondientes a JavaScript-->
<script>
import axios from "axios";
import Swal from "sweetalert2";
export default {
  name: "HelloWorld",
  data() {
    return {
      name: "",
      address: "",
      price: "",
      calification: "",
      msg: "Welcome to Your Coworking Catalog",
      chips: ["Conferencias", "Cafe", "Sofá"],
      dialog: false,
      rules: {
        required: value => !!value || "Obligatorio",
        counter: value => value.length <= 30 || "Max 30 caracteres"
      },

      headers: [
        {
          align: "left",
          sortable: false,
          value: "nombre"
        },
        { text: "Nombre", value: "nombre" },
        { text: "Direccion", value: "direccion" },
        { text: "Precio", value: "precio" },
        { text: "Calificacion", value: "calificacion" },
        { text: "Accciones", value: "acciones" }
      ],
      coworks: [],

      cards: {
        nombre: "",
        direccion: "",
        precio: "",
        calificacion: ""
      }
    };
  },
  methods: {
    remove(item) {
      this.chips.splice(this.chips.indexOf(item), 1);
      this.chips = [...this.chips];
    },

    getCoworkings() {
      const path = "http://127.0.0.1:7000/api/v1.0/sitios/";
      axios
        .get(path)
        .then(response => {
          this.coworks = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },

    postCoworking() {
      const path = "http://127.0.0.1:7000/api/v1.0/sitios/";
      axios({
        method: "post",
        url: path,
        data: this.cards
      })
        .then(response => {
          console.log(response);
          Swal.fire({
            title: "Creado!",
            type: "success",
            confirmButtonText: "Volver"
          });
        })
        .catch(error => {
          console.log(error);
            Swal.fire({
            title: "Hubo un error en la creación, verifica los campos",
            type: "error",
            confirmButtonText: "Volver"
          });
        });
    }
  },

  created() {
    this.getCoworkings();
  },

  computed: {
    formTitle() {
      return this.editedText === -1 ? "New coworking" : "Edit Coworking";
    }
  }
};
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
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
