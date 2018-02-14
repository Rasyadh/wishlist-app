<template>
  <div class="app">
    <div class="container">
      <h1 class="title has-text-centered">WishList App</h1>
      <create-wish @create-wish="createWish"></create-wish>
      <hr>
      <wish-list :wishes="wishList"></wish-list>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import CreateWish from "./components/CreateWish";
import WishList from "./components/WishList";

export default {
  name: "App",
  components: {
    CreateWish,
    WishList
  },
  data() {
    return {
      wishList: []
    };
  },
  created() {
    axios
      .get("http://127.0.0.1:5000/api/wishlist")
      .then(response => {
        this.wishList = response.data;
        for (let key in this.wishList) {
          if (this.wishList[key].done == 'False') {
            this.wishList[key].done = false;
          }
          else if (this.wishList[key].done == 'True') {
            this.wishList[key].done = true;
          }
        }
        console.log(this.wishList);
      })
      .catch(error => {
        console.log(error);
      });
  },
  methods: {
    createWish(newWish) {
      axios
        .post("http://127.0.0.1:5000/api/wishlist", {
          wish: newWish.wish,
          done: newWish.done
        })
        .then(response => {
          const keys = Object.keys(response.data);
          Vue.set(this.wishList, keys, newWish);
          console.log(this.wishList[keys]);
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style>
.app {
  padding: 2em;
}
</style>
