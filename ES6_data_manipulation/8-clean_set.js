export default function cleanSet(set, startString) {
  if (startString === '') return '';

  try {
    return [...set]
      .filter((str) => typeof str === 'string' && str.startsWith(startString))
      .map((str) => str.replace(startString, ''))
      .join('-');
  } catch (e) {
    return '';
  }
}
