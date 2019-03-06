<template>
    <div class="register_form" id="Register">
        <h2 class="login-heading">Registro</h2>
        <form action="#" @submit.prevent="login">

            <div class="form_control">
                <v-text-field label="Name"  for="email"></v-text-field>
            </div>

            <div class="form_control">
                <v-text-field label="Email" for="password"></v-text-field>  
            </div>

            <div class="form_control">
                <v-text-field label="password" for="password"></v-text-field>   
            </div>

            <div class="form_control">
                <v-btn color="blue"  type="submit" class="btn_submit">Create account</v-btn>
            </div>
        </form>
    </div>
</template>

<style>
#Register{
    width: 300px;
    height: 50%;
    margin-left: 40%;
}
</style>

