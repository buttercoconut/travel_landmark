<template>
  <div>
    <h2>Landmark List</h2>
    <ul>
      <li v-for="landmark in landmarks" :key="landmark.id">
        {{ landmark.name }} - {{ landmark.description }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'LandmarkList',
  data() {
    return {
      landmarks: [],
    }
  },
  mounted() {
    fetch('/api/landmarks')
      .then(res => res.json())
      .then(data => {
        this.landmarks = data
      })
  },
}
</script>
