import { PieChart } from "@mui/x-charts/PieChart";
import { useEffect, useState } from "react";

export default function PieChartAntennaFail() {
  const [values, setValues] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/antennas/states")
      .then((response) => response.json())
      .then((data) => {
        const comm_ok = data.filter(item => {
            return item.state
        }).length
        const total=data.length
        setValues([
            {value: comm_ok/total*100, label: 'OK', color: 'lightgreen'},
            {value: (total - comm_ok)/total*100, label: 'Falla', color: 'red'}
        ]);
      });
  }, []);

  if (values.length == 0) return "";

  return (
    <PieChart
        height={300}
        slotProps={{
            legend: {
              direction: 'row',
              position: { vertical: 'top', horizontal: 'middle' },
              padding: 5,
            },
          }}
      series={[
        {
          data: values,
          innerRadius: 30,
          outerRadius: 100,
          paddingAngle: 5,
          cornerRadius: 5,
          startAngle: -90,
          endAngle: 180,
          cx: 150,
          cy: 150,
        },
      ]}
    />
  );
}
