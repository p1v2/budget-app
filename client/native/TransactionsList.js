import React, { Component } from 'react';
import { View, FlatList } from 'react-native';
import { ListItem} from "react-native-material-ui";
import { connect } from 'react-redux';

import { listTransactions } from './reducer';

class TransactionsList extends Component {
  componentDidMount() {
    this.props.listTransactions();
  }
  renderItem = ({ item }) => (
      <View>
        <ListItem
          divider
          centerElement={{
            primaryText: item.name,
            secondaryText: item.amount + item.amount_currency,
          }}
        />
      </View>
  );
  render() {
    const { transactions } = this.props;
    return (
      <FlatList
        data={transactions}
        renderItem={this.renderItem}
      />
    );
  }
}

const mapStateToProps = state => {
  let storedTransactions = state.transactions.map(transaction => ({ key: transaction.id, ...transaction }));
  return {
    transactions: storedTransactions,
  };
};

const mapDispatchToProps = {
  listTransactions: listTransactions
};

export default connect(mapStateToProps, mapDispatchToProps)(TransactionsList);