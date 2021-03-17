<template>
<div id="H1xWWcKhy_">
  <mdc-textfield class="Syl9-9t2yO" id='user' label="Username" value="" type="text" rows="100" cols="100"></mdc-textfield>
  <mdc-textfield class="rJ9Sctnku" id = 'pass' label="Password" value="" type="password" rows="100" cols="100"></mdc-textfield>
  <button class="ryiT8K4ld" @click="btnLogin_Click">Login</button>
  <a href="/#/createAccount"> <button class="H1ppLYVgu">Create Account</button> </a>

</div>
</template>

<script>
export default {

  name: 'login',

  methods: {

        btnLogin_Click: function (event) {
        // const requestOptions = 
        // {
        //   method: "GET",
        // };

        
        // fetch("http://localhost:8000/med/intro", requestOptions)
        //   .then(response => response.json())
        //   .then(body => console.log(body['message']))
        
        var user = document.getElementById('user').children[0].children[0].value;
        var pass = document.getElementById('pass').children[0].children[0].value;

        var userFieldName = 'username';
        var passFieldName = 'password';

        var request = {};
        request[userFieldName] = user;
        request[passFieldName] = pass;


        const requestOptions = {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(request)
        };

        fetch("http://localhost:8000/dj-rest-auth/login/", requestOptions)
          .then(response => {
            if (response.ok) return response.json();
            else throw new Error('Wrong Credentials');
          })
          .then(body => this.$router.push('/homescreen'))
          .catch((error) => { alert('Wrong Credentials'); });
        //alert('Hello ' + 'name' + '!'); 
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#H1xWWcKhy_ {
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

.ryiT8K4ld {
  overflow: hidden;
  text-overflow: ellipsis;
  position: absolute;
  width: 128px;
  height: 30px;
  top: 260px;
  left: 194px;
}

.H1ppLYVgu {
  overflow: hidden;
  text-overflow: ellipsis;
  position: absolute;
  width: 200px;
  height: 40px;
  top: 465px;
  left: 71px;
}

</style>
