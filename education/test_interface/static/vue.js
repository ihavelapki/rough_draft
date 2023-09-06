Vue.component('video-player', {
  data() {
    return {
      videoUrl: 'https://example.com/video.mp4',
      playbackRate: 1.0,
      volume: 0.5
    }
  },
  template: `
    <div>
      <video :src="videoUrl" :playbackRate="playbackRate" :volume="volume"></video>
      <input type="range" v-model="playbackRate" min="0.5" max="2.0" step="0.1">
      <input type="range" v-model="volume" min="0.0" max="1.0" step="0.05">
    </div>
  `
})
