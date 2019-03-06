<!--Código correspondiente a la creación de los elementos que se encontraran en la página-->
<template>
    <div class="register_form" id="Register">
        <h2 class="login-heading">Registro</h2>
        <form action="#" @submit.prevent="login">

            <!--Se crea la caja de texto para que se ingrese el nombre de usuario-->
            <div class="form_control">
                <v-text-field label="Name"  for="email"></v-text-field>
            </div>

            <!--Se crea la caja de texto para que se ingrese el email del usuario-->
            <div class="form_control">
                <v-text-field label="Email" for="password"></v-text-field>  
            </div>

            <!--Se crea la caja de texto para que se ingrese la contraseña del usuario-->
            <div class="form_control">
                <v-text-field label="password" for="password"></v-text-field>   
            </div>

            <!--Se crea el boton para que el usuario indique que ya ingreso toda la información y quiere crear la cuenta-->
            <div class="form_control">
                <v-btn color="blue"  type="submit" class="btn_submit">Create account</v-btn>
            </div>
        </form>
    </div>
</template>

<!--Modelo para el retorno de los datos guardados, métodos. Todos los códigos correspondientes a JavaScript-->
<script>
export default {

}
</script>

<!--Código que se encarga de manejar el estilo de la página y los elementos que estan en ella-->
<style>
#Register{
    width: 300px;
    height: 50%;
    margin-left: 40%;
}
</style>

