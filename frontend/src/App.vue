<template>
  <div class="app">
    <div class="container">
      <h1 class="title has-text-centered">WishList App</h1>
      <create-wish @create-wish="createWish"></create-wish>
      <hr>
      <div class="has-text-centered" v-show="isLoading">
        <span class="icon has-text-info is-medium">
          <i class="fas fa-2x fa-spinner fa-pulse"></i>
        </span>
      </div>
      <p v-show="isFail" class="subtitle has-text-centered">Can't load your wish list.</p>
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
      wishList: [],
      isLoading: true,
      isFail: false
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
        this.isLoading = false;
        console.log(this.wishList);
      })
      .catch(error => {
        this.isFail = true;
        this.isLoading = false;
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
