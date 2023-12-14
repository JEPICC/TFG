import { useEffect, useState } from "react";
import { Box } from "@mui/material";
import { BarChart } from '@mui/x-charts/BarChart';

export default function BarChartProd() {
  const [values, setValues] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/wells/calculate/daily")
      .then((response) => response.json())
      .then((data) => {
        const dataPlus = data.map((item) => ({
          date: new Date(item._id).toLocaleDateString(),
          value: item.daily,
        }));
        setValues(dataPlus);
      });
  }, []);

  if (values.length == 0) return "";

  return (
    <Box sx={{ width: "100%" }}>
      <BarChart
      colors={['brown']}
      height={250}
      dataset={values}
      xAxis={[{ scaleType: 'band', dataKey: 'date' }]}
      series={[{ dataKey: 'value'}]}
      leftAxis={null}      
    />
    </Box>
  );
}
