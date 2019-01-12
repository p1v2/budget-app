export const GET_TRANSACTIONS = 'budget/transactions/LOAD';
export const GET_TRANSACTIONS_SUCCESS = 'budget/transactions/LOAD_SUCCESS';
export const GET_TRANSACTIONS_FAIL = 'budget/transactions/LOAD_FAIL';

export default function reducer(state = { transactions: [] }, action) {
  switch (action.type) {
    case GET_TRANSACTIONS:
      return { ...state, loading: true };
    case GET_TRANSACTIONS_SUCCESS:
      return { ...state, loading: false, transactions: action.payload.data };
    case GET_TRANSACTIONS_FAIL:
      return {
        ...state,
        loading: false,
        error: 'Error while fetching transactions'
      };
    default:
      return state;
  }
}

export function listTransactions() {
  return {
    type: GET_TRANSACTIONS,
    payload: {
      request: {
        url: `/spends`
      }
    }
  };
}