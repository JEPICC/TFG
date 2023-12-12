import Box from "@mui/material/Box";
import { useEffect, useState } from "react";
import useInterval from "../hooks/useInterval";
import { Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Typography } from "@mui/material";

export default function Comunication() {
  const [dataState, setDataState] = useState()
  const [dataFailure, setDataFailure] = useState()

  const loadAntennas = async () => {
      const response = await fetch("http://localhost:8000/antennas/states");
      const data = await response.json();
      const sortedData = data.sort((o1, o2) => (o1.id > o2.id ? 1 : -1));
      const formatedData = sortedData.map(element => {
        return {id: element.id,
                state: element.state ? "OK" : "Falla",
                time: new Date(element.time).toLocaleString()}
      });
      setDataState(formatedData);
  };

  const loadFailures = async () => {
    const response = await fetch("http://localhost:8000/antennas/failures");
    const data = await response.json();
    //const sortedData = data.sort((o1, o2) => (o1.id > o2.id ? 1 : -1));
    const formatedData = data.map(element => {
      return {tag: element.tag,
              code: element.states.codigo_error,
              description: element.states.descripcion,
              time: new Date(element.states.timestamp).toLocaleString()}
    });
    setDataFailure(formatedData);
    console.log('FAlla');
};

  useEffect(()=>{
    loadAntennas()
    loadFailures()
  },[])

  useInterval(loadAntennas, 5000)
  useInterval(loadFailures, 5000)

  if (!dataState || !dataFailure) return "";

  return (
    <Box  display="flex" flexDirection="column" alignItems="center">
      <Typography variant="h4" component="h2" sx={{mb:3}}>Estado de Antenas:</Typography>
      <TableContainer component={Paper} sx={{ maxWidth:800}}>
      <Table sx={{ minWidth: 650}} stickyHeader aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>TAG</TableCell>
            <TableCell align="center">ESTADO</TableCell>
            <TableCell align="center">FECHA, HORA</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {dataState.map((row, index) => (
            <TableRow
              key={index}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">{row.id}</TableCell>
              <TableCell align="center">{row.state}</TableCell>
              <TableCell align="center">{row.time}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
      <Typography variant="h6" component="h6" sx={{mt:5, mb:2}}>
              Ultimas 10 Fallas:
            </Typography>
      <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} stickyHeader size="small" aria-label="a dense table">
        <TableHead>
          <TableRow>
            <TableCell>TAG</TableCell>
            <TableCell align="center">Codigo Error</TableCell>
            <TableCell align="left">Description</TableCell>
            <TableCell align="left">Fecha</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {dataFailure.map((row, index) => (
            <TableRow
              key={index}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.tag}
              </TableCell>
              <TableCell align="center">{row.code}</TableCell>
              <TableCell align="left">{row.description}</TableCell>
              <TableCell align="left">{row.time}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
    </Box>
  );
}
