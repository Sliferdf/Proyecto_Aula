<!--Codigo correspondiente a la creacion de los elementos que se encontraran en la pagina-->
<template>
    <div class="login_form" id="login">
        <h2 class="login-heading">Login</h2>
        <form action="#" @submit.prevent="login">

            <div class="form_control">
                <!--Se crea el campo de texto para que se indique el usuario o email, se indica que tipo es la informacion y se guarda  en un v-model-->
                <label for="email">Username/Email</label>
                <input type="email" name="username" id="username" class="login_input" v-model="username">
            </div>
            
            <div class="form_control">
                <!--Se crea el campo de texto para que se indique la contraseña del usario, se indica que tipo es la informacion y se guarda  en un v-model-->
                <label for="password">password</label>
                <input type="password" name="password" id="password" class="login_input" v-model="password">   
            </div>

            <div class="form_control">
                <!--Se crea el boton para poder logearse e ingresar-->
                <v-btn color="blue"  type="submit" class="btn_submit">Login</v-btn>
            </div>
        </form>
    </div>
</template>

<!--Se indica como se guarda y devuelve la infromacion que el usuario ha guardado. Esta todo el codigo correspondiente a JavaScript-->
<script>
export default {
    name: 'login',
    data(){
        return {
            username: '',
            password:'',
        }
    }, 
    //Se ingresan los metodos que se van a usar la informacion que se ha ingresado
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

<!--Codigo que se encarga de manejar el estilo de la pagina y los elementos que estan en ella-->
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
    border: solid 1px;
    border-radius: 10px;
}

h2 {
    align-content: left;
}

.login_form{
    border: solid 1px;
    border-radius: 10px;
}
</style>

