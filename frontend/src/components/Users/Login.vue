<template>
    <div class="login_form" id="login">
        <h2 class="login-heading">Login</h2>
        <form action="#" @submit.prevent="login">

            <div class="form_control">
                <label for="email">Username/Email</label>
                <input type="email" name="username" id="username" class="login_input" v-model="username">
            </div>

            <div class="form_control">
                <label for="password">password</label>
                <input type="password" name="password" id="password" class="login_input" v-model="password">   
            </div>

            <div class="form_control">
                <v-btn color="blue"  type="submit" class="btn_submit">Login</v-btn>
            </div>
        </form>
    </div>
</template>
<script>
export default {
    name: 'login',
    data(){
        return {
            username: '',
            password:'',
        }
    }, 
    methods: {
        login (){
            this.$store.dispatch('retrieveToken', {
                username: this.username,
                password: this.password,
            })
        }
    }
}
</script>

<style>
#login{
    margin-left: 30%;
    width: 50%;
    height: 50%;
}
.form_control{
    padding: 10px;
    width: 80%;
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

/*.login_form{
    align-items:center;
    background-color: aqua;
}*/

</style>

