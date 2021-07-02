import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
      themes: {
        light: {
          primary: colors.lightBlue.lighten3,
          secondary: colors.grey.lighten3,
          active: colors.lightBlue.lighten4,
          accent: colors.shades.black,
          error: colors.red.accent3,
          bar: colors.orange,
          background: colors.shades.white, // Not automatically applied
        },
        dark: {
          primary: colors.blue.lighten3, 
          background: colors.indigo.base, // If not using lighten/darken, use base to return hex
        },
      },
    },
  })
  