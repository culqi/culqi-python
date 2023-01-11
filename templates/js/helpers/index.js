export const formatAmount = (amount) => {
    const amountStringified = amount.toString();
    const decimalAmount = amountStringified.length - 2;
    return `${amountStringified.slice(0, decimalAmount)}.${amountStringified.slice(decimalAmount)}`
}