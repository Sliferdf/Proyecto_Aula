<!--Código correspondiente a la creación de los elementos que se encontraran en la página-->
<template>
    <div class="login_form" id="login">
        <h2 class="login-heading">Login</h2>
        <form action="#" @submit.prevent="login">

            <div class="form_control">
                <!--Se crea el campo de texto para que se indique el usuario o email, se indica que tipo es la información y se guarda  en un v-model-->
                <v-text-field label="Username/Email" type="email" name="username" id="username" class="login_input" v-model="username"></v-text-field>
            </div>
            
            <div class="form_control">
                <!--Se crea el campo de texto para que se indique la contraseña del usario, se indica que tipo es la información y se guarda  en un v-model-->
                <v-text-field label="Password" type="password" name="username" id="username" class="login_input" v-model="password"></v-text-field>
            </div>

            <div class="form_control">
                <!--Se crea el boton para poder logearse e ingresar-->
                <v-btn color="blue"  type="submit" class="btn_submit">Login</v-btn>
            </div>
        </form>
    <div class="nav">
        <router-link to="/">Ir al inicio</router-link>
    </div>
    <div class="nav">
        <router-link to="/register">¿Aún no estás registrado? Registrate desde aquí</router-link>
    </div>      
    </div>
</template>

<!--Se indica como se guarda y devuelve la información que el usuario ha guardado. Esta todo el código correspondiente a JavaScript-->
<script>
export default {
    name: 'login',
    data(){
        return {
            username: '',
            password:'',
        }
    }, 
    //Se ingresan los métodos que se van a usar la información que se ha ingresado.
    methods: {
        login (){
            this.$main.dispatch('retrieveToken', {
                username: this.username,
                password: this.password,
            })
        }
    }
}
</script>

<!--Código que se encarga de manejar el estilo de la página y los elementos que estan en ella-->
<style>
#login{
    width: 300px;
    height: 50%;
    margin-left: 40%;
}
.form_control{
    padding: 10px;
    width: 100%;
    height: 80%;
}
.btn_submit{
    width: 80%;
    height: 40px;
}

.login_input{
    border: 1px;
    width: 100%;
    height: 40px;
}

h2 {
    align-content: left;
}

</style>

