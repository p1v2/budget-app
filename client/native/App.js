import React, { Component } from 'react';
import { View } from 'react-native';
import { createStore, applyMiddleware } from 'redux';
import { Provider } from 'react-redux';
import axios from 'axios';
import axiosMiddleware from 'redux-axios-middleware';
import { Font, AppLoading } from 'expo';

import { Toolbar, ThemeContext, getTheme } from 'react-native-material-ui';

import reducer from './reducer';
import TransactionsList from './TransactionsList';
import {getStatusBarHeight} from "react-native-status-bar-height";

const client = axios.create({
  baseURL: 'https://budget-vitalii.herokuapp.com/api',
  responseType: 'json'
});

const uiTheme = {
  palette: {
    primaryColor: '#1E4A43',
    toolbar: {
    container: {
      height: 50,
    },
  },
  }
};

const store = createStore(reducer, applyMiddleware(axiosMiddleware(client)));

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = { loading: true };
  }

  async componentWillMount() {
    await Font.loadAsync({
      Roboto: require("native-base/Fonts/Roboto.ttf")
    });
    this.setState({ loading: false });
  }

  render() {
    if (this.state.loading) {
      return <AppLoading />;
    }
    return (
        <ThemeContext.Provider value={getTheme(uiTheme)}>
      <Provider store={store}>
        <View>
          <Toolbar
              centerElement="Transactions List"
              style={{ marginTop: getStatusBarHeight(true) }}
          />
          <TransactionsList />
        </View>
      </Provider>
        </ThemeContext.Provider>
    );
  }
}

