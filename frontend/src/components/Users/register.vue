<!--Código correspondiente a la creación de los elementos que se encontraran en la página-->
<template>
    <div class="register_form" id="register" >
        <h2 class="login-heading">Registro</h2>
        <form action="#">
            <!--Se crea la caja de texto para que se ingrese el nombre de usuario-->
            <div class="form_control ">
                <v-text-field label="Name"  for="name" v-model="nuevaUsername" ></v-text-field>
            </div>

            <!--Se crea la caja de texto para que se ingrese el email del usuario-->
            <div class="form_control">
                <v-text-field label="Email"  type="email" v-model="nuevaEmail" ></v-text-field>  
            </div>

            <!--Se crea la caja de texto para que se ingrese la contraseña del usuario-->
            <div class="form_control">
                <v-text-field label="password" for="password" type="password" v-model="nuevaPassword"></v-text-field>   
            </div>

            <!--Se crea el boton para que el usuario indique que ya ingreso toda la información y quiere crear la cuenta-->
            <div class="form_control">
                <v-btn color="blue"  type="submit" class="btn_submit" @click="agregarUsername">Create account</v-btn>
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

export default {
    name: 'register',
    data(){
        return {
        username: [],
        nuevaUsername: '',
        email: [],
        nuevaEmail: '',
        password: [],
        nuevaPassword: '',
        }
    },
    methods: {
        //Este método se encarga de guardar los elementos en la base de datos local
        agregarUsername: function () {
            this.username.push({
                name: this.nuevaUsername,
                correo: this.nuevaEmail,
                pass: this.nuevaPassword
            });
            this.nuevaUsername = '';
            this.nuevaEmail = '';
            this.nuevaPassword = '';
            //Se guardar a los elementos en la base de datos local
            localStorage.setItem('username',
                JSON.stringify(this.username));
         },                

        created: function (index) {
        var datosUsername = JSON.parse(localStorage.getItem('Username'));
        var datosEmail = JSON.parse(localStorage.getItem('Email'));
        var datosPassword = JSON.parse(localStorage.getItem('Password'));
        if (datosUsername === null || datosEmail === null || datosPassword === null ) {
            this.Username = [];
            this.Email = [];
            this.Password = [];
        } else {
            this.actividades = datosActividades;
        }

    }
    
    }
}
</script>

<!--Código que se encarga de manejar el estilo de la página y los elementos que estan en ella-->
<style>
#register{
    width: 300px;
    height: 50%;
    margin-left: 40%;
}

</style>

