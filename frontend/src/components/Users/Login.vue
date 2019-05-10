<!--Código correspondiente a la creación de los elementos que se encontraran en la página-->
<template>
    <div class="login_form" id="login">
        <h2 class="login-heading">Login</h2>
        <form action="#" @submit.prevent="login">

            <div class="form_control">
                <!--Se crea el campo de texto para que se indique el usuario o email, se indica que tipo es la información y se guarda  en un v-model-->
                <v-text-field 
                v-model="username"
                :error-messages="userNameError" 
                id="username" 
                type="email"
                class="login_input" 
                label="Username/Email"
                required 
                @input="$v.username.$touch()"
                @blur="$v.username.$touch()"
                ></v-text-field>
            </div>
            
            <div class="form_control">
                <!--Se crea el campo de texto para que se indique la contraseña del usario, se indica que tipo es la información y se guarda  en un v-model-->
                <v-text-field 
                v-model="password" 
                :error-messages="passwordError"
                label="Password" 
                type="password"
                class="login_input" 
                id="username" 
                required
                @input="$v.password.$touch()"
                @blur="$v.password.$touch()"
                ></v-text-field>
            </div>

            <div class="form_control">
                <!--Se crea el boton para poder logearse e ingresar-->
                <v-btn black color="blue"  type="submit" class="btn_submit" @click="submit">Login</v-btn>
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
import Swal from 'sweetalert2'
import { validationMixin } from 'vuelidate'
import { required, email} from 'vuelidate/lib/validators'

export default {
    mixins: [validationMixin], 
    validations: {
        username: { required, email},
        password: {required}
    },
    data: () => ({
        username: '',
        password: ''
    }),
    computed: {
        userNameError() {
            const errors = []
            if (!this.$v.username.$dirty) return errors
            !this.$v.username.required && errors.push("El email es requerido")
            !this.$v.username.email && errors.push("El email debe de ser valido")
            return errors
        },
        passwordError(){
            const errors = []
            if (!this.$v.password.$dirty) return errors
            !this.$v.password.required && errors.push("La contraseña  es requerida")
            return errors
        }
    },
    //Se ingresan los métodos que se van a usar la información que se ha ingresado.
    methods: {
        submit () {
            this.$v.touch()
        },
        clear() {
            this.$v.$reset()
            this.$v.username = ''
            this.$v.password = ''
        },
        /** 
        login: function (){
            if (this.username == JSON.parse(localStorage.getItem('email')) && this.password== JSON.parse(localStorage.getItem('password'))) {
                 Swal.fire({
                    title: 'Estás registrado!',
                    text: 'Puedes ingresar',
                    type: 'success',
                    confirmButtonText: 'Redirigir'
                })
            }
            else{
                Swal.fire({
                    title: 'Error!',
                    text: 'Aún no te encuentras registrado',
                    type: 'error',
                    confirmButtonText: 'Reintentar'
                })
            }
        },*/
    },
    name: 'login'
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
