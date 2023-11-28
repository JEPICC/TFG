import { LineChart } from '@mui/x-charts/LineChart';


export default function SingleLineChart() {
    return (
      <LineChart
        xAxis={[{ data: [1, 2, 3, 5, 8, 10] }]}
        series={[
          {
            data: [2, 5.5, 2, 8.5, 1.5, 5],

          },
          {data: [1, 8, 9, 4, 5, 8]}
        ]}
        width={500}
        height={300}
      />
    );
  }