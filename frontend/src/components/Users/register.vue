
<!--Código correspondiente a la creación de los elementos que se encontraran en la página-->
<template>
  <div class="register_form" id="register">
    <h2 class="login-heading">Registro</h2>
    <form action="#">
      <!--Se crea la caja de texto para que se ingrese el nombre de usuario-->
      <div class="form_control">
        <v-text-field
          v-model="nuevo.name"
          :error-messages="newUserNameError"
          :counter="30"
          label="Name"
          for="name"
          required
          @input="$v.nuevaUsername.$touch()"
          @blur="$v.nuevaUsername.$touch()"
        ></v-text-field>
      </div>

      <!--Se crea la caja de texto para que se ingrese el email del usuario-->
      <div class="form_control">
        <v-text-field
          v-model="nuevo.email"
          :error-messages="newEmailError"
          label="Email"
          type="email"
          required
          @input="$v.nuevaEmail.$touch()"
          @blur="$v.nuevaEmail.$touch()"
        ></v-text-field>
      </div>

      <!--Se crea la caja de texto para que se ingrese la contraseña del usuario-->
      <div class="form_control">
        <v-text-field
          v-model="nuevo.passw"
          :error-messages="newPasswordError"
          label="password"
          for="password"
          type="password"
          required
          @input="$v.nuevaPassword.$touch()"
          @blur="$v.nuevaPassword.$touch()"
        ></v-text-field>
      </div>

      <!--Se crea el boton para que el usuario indique que ya ingreso toda la información y quiere crear la cuenta-->
      <div class="form_control">
        <v-btn color="blue" type="submit" class="btn_submit" @click="postRegister">Create account</v-btn>
      </div>
    </form>

    <div class="nav">
      <router-link to="/">Ir al inicio</router-link>
    </div>
    <div class="nav">
      <router-link to="/login">¿Ya estás registrado? Ingresa desde aquí</router-link>
    </div>
  </div>
</template>

<!--Modelo para el retorno de los datos guardados, métodos. Todos los códigos correspondientes a JavaScript-->
<script>
import { validationMixin } from "vuelidate";
import { required, maxLength, email } from "vuelidate/lib/validators";
import axios from "axios";
import Swal from "sweetalert2";

export default {

  mixins: [validationMixin],
  validations: {
    nuevaUsername: { required, maxLength: maxLength(30) },
    nuevaEmail: { required, email },
    nuevaPassword: { required }
  },

  data: () => ({
    username: [],
    nuevaPassword: "",
    nuevaUsername: "",
    nuevaEmail: "",

    nuevo: {
    name: "",
    email: "",
    passw: ""
  },
  }),
  computed: {
    newUserNameError() {
      const errors = [];
      if (!this.$v.nuevaUsername.$dirty) return errors;
      !this.$v.nuevaUsername.required && errors.push("El nombre es requerido");
      !this.$v.nuevaUsername.maxLength &&
        errors.push("El nombre debe tener menos de 30 caracteres");
      return errors;
    },
    newEmailError() {
      const errors = [];
      if (!this.$v.nuevaEmail.$dirty) return errors;
      !this.$v.nuevaEmail.required && errors.push("El email es requerido");
      !this.$v.nuevaEmail.email && errors.push("El email debe de ser valido");
      return errors;
    },
    newPasswordError() {
      const errors = [];
      if (!this.$v.nuevaPassword.$dirty) return errors;
      !this.$v.nuevaPassword.required &&
        errors.push("La contraseña es requerida");
      return errors;
    }
  },
  
  //Se ingresan los métodos que van a usar la información qu ingresa el usuario
  methods: {
    submit() {
      this.$v.touch();
    },

    postRegister() {
      const path = "http://127.0.0.1:8000/api/registro/nuevos/";
      axios({
        method: "post",
        url: path,
        data: this.nuevo
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
            title: "No se pudo completar el registro",
            type: "error",
            confirmButtonText: "Volver"
          });
        });
    }
  }
};
</script>

<!--Código que se encarga de manejar el estilo de la página y los elementos que estan en ella-->
<style>
#register {
  width: 300px;
  height: 50%;
  margin-left: 40%;
}
</style>

