<template>
<div id="ry3eiK3kO" v-bind:style="{backgroundImage:'url(/static/backgroundSD5.jpg)'}">
  <mdc-textfield class="usernameTextField" label="Username" value="" type="text" rows="100" cols="100"></mdc-textfield>
  <mdc-textfield class="passwordTextField" label="Password" value="" type="text" rows="100" cols="100"></mdc-textfield>
  <mdc-textfield class="confirmPasswordTextField" label="Confirm Password" value="" type="text" rows="100" cols="100"></mdc-textfield>
  <mdc-textfield class="emailTextField" label="Email" value="" type="text" rows="100" cols="100"></mdc-textfield>
  <mdc-textfield class="AgeTextField" label="Age" value="" type="text" rows="100" cols="100"></mdc-textfield>
  <mdc-textfield class="WeightTextField" label="Weight" value="" type="text" rows="100" cols="100"></mdc-textfield>
  <a href="/#/"> <button class="backButton">Back</button> </a>
  <a href="/#/"> <button class="loginButton">Login</button> </a>

</div>
</template>

<script>
export default {
  name: 'create-account'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#ry3eiK3kO {
  --mdc-theme-primary: #673ab7;
  --mdc-theme-secondary: #f44336;
  --mdc-theme-background: #ffffff;
  position: relative;
  margin: auto;
  background-color: #ffffff;
  overflow: hidden;
  width: 100%;
  height: 100%;
}
.backButton {
  overflow: hidden;
  text-overflow: ellipsis;
  position: absolute;
  width: 66px;
  height: 27px;
  top: 13px;
  left: 10px;
}

.loginButton {
  overflow: hidden;
  text-overflow: ellipsis;
  position: absolute;
  width: 66px;
  height: 27px;
  top: 400px;
  left: 179px;
;
}


.usernameTextField{
  --mdc-theme-primary: rgb(205, 133, 232);
  --mdc-theme-background: rgb(0, 0, 0);
  position: absolute;
  width: 160px;
  height: 36px;
  top: 50px;
  left: 75px;
}

.passwordTextField{
  --mdc-theme-primary: rgb(205, 133, 232);
  --mdc-theme-background: rgb(0, 0, 0);
  position: absolute;
  width: 160px;
  height: 36px;
  top: 100px;
  left: 75px;
}

.confirmPasswordTextField{
  --mdc-theme-primary: rgb(205, 133, 232);
  --mdc-theme-background: rgb(0, 0, 0);
  position: absolute;
  width: 160px;
  height: 36px;
  top: 150px;
  left: 75px;
}

.emailTextField{
  --mdc-theme-primary: rgb(205, 133, 232);
  --mdc-theme-background: rgb(0, 0, 0);
  position: absolute;
  width: 160px;
  height: 36px;
  top: 200px;
  left: 75px;
}

.AgeTextField{
  --mdc-theme-primary: rgb(205, 133, 232);
  --mdc-theme-background: rgb(0, 0, 0);
  position: absolute;
  width: 160px;
  height: 36px;
  top: 250px;
  left: 75px;
}

.WeightTextField{
  --mdc-theme-primary: rgb(205, 133, 232);
  --mdc-theme-background: rgb(0, 0, 0);
  position: absolute;
  width: 160px;
  height: 36px;
  top: 300px;
  left: 75px;
}

</style>
