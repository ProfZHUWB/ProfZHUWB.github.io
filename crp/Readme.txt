Files

  Caserta2009/    Result of our algorithm on instances created by Caserta et. al.
    caserta.txt   Instances created by Caserta et. al., converted to our input format.
                  We assume the maximum height of any stack is h + 2
                  
    IDA-R         Solutions found by our IDA*-R
                        
    IDA-UM        Solutions found by our IDA*-UM
    
  Lee2010/                    Result of our algorithm on instances created by Lee and Lee.
    Lee2010-Random.txt        Random instances created by Lee and Lee, 10 instances with one bay are converted to our input format.
    Lee2010-Upsidedown.txt    Upsidedown instances created by Lee and Lee, 4 instances with one bay are converted to our input format.
    IDA-R                     
      Random/                 Solutions foudn by our IDA*-R for random instances
                                          Instance Name (by Lee and Lee),   Solution File
                                            R011606_0070_001                  sol-6-16-1.txt
                                            R011606_0070_002                  sol-6-16-2.txt
                                            R011606_0070_003                  sol-6-16-3.txt
                                            R011606_0070_004                  sol-6-16-4.txt
                                            R011606_0070_005                  sol-6-16-5.txt
                                            R011608_0090_001                  sol-8-16-1.txt
                                            R011608_0090_002                  sol-8-16-2.txt
                                            R011608_0090_003                  sol-8-16-3.txt
                                            R011608_0090_004                  sol-8-16-4.txt
                                            R011608_0090_005                  sol-8-16-5.txt
      Upsidedown/             Solutions found by our IDA*-R for upsidedown instance
                                          Instance Name (by Lee and Lee),   Solution File
                                            U011606_0070_001                  sol-6-16-1.txt
                                            U011606_0070_002                  sol-6-16-2.txt
                                            U011608_0090_001                  sol-8-16-1.txt
                                            U011608_0090_002                  sol-8-16-2.txt
    IDA-UM                    
      Random/                 Solutions foudn by our IDA*-UM for random instances
      Upsidedown/             Solutions found by our IDA*-UM for upsidedown instance

                        
  Zhuwb2011/  Result of running our algorithm (1 CPU second) on our own instances
    data.txt            12500 Generated Instances
    solFileFormat.txt   Solution file format
    summary.xlsx        Excel workbook summarizes the result of various algorithm for each individual instances. It includes the following columns
                            Instances                       describe the characteristic of instances
                              case #                          the ID of instance
                              S                               number of stacks in a bay
                              T                               number of tiers in a bay
                              N                             number of containers in the initial configuration
                            Restricted (Best Known)         The best known result from all experiments we have done, including the result reported by running IDA_PR+_LB3_PR4 on high performance server
                              LB                              Lower bound of number of relocations
                              Reloc                           Number of relocations of best known solution
                            IDA*-R (2^30 nodes)	            The best solution found by running IDA*-R on high performance server, the number of node explored is limited to 2^30
                              Reloc                           Number of relocations of best solution
                              time (S)                        CPU time taken to find the best solution
                            IDA*-R (Time Limit 1S) The best solution found by running IDA*-R on Pentium 4, with 1 CPU second
                              Reloc                           Number of relocations of the best solution found
                              time (S)                        CPU time taken to find the best solution
                              optimal?                        1: indicates the best solution found is optimal; 0: otherwise
                              Gap to LB                       The gap between the best solution found and the best known LB
                              Gap to Best                     The gap between the best solution found and the best known solution
                            Unrestricted (Best Known)	      The best known result from all experiments we have done, including the result reported by running IDA_PU+_LB1_PU2 on high performance server
                            IDA*-U (2^30 Nodes)	            The best solution found by running IDA*-U on high performance server, the number of node explored is limited to 2^30
                            IDA*-U (Time Limit 1S)	        The best solution found by running IDA*-U on Pentium 4, with 1 CPU second
                            IDA*-UM (Time Limit 1S)	        The best solution found by running IDA*-UM on Pentium 4, with 1 CPU second
                            IDA*-UM3 (Time Limit 1S)		    The best solution found by running IDA*-UM3 on Pentium 4, with 1 CPU second

    time=1S             Solutions obtained on Pentium 4, where each instances is given 1 CPU second
      IDA-R/                Solutions files produced by IDA*-R
      IDA-U/                Solutions files produced by IDA*-U
      IDA-UM/               Solutions files produced by IDA*-UM
      IDA-UM3/              Solutions files produced by IDA*-UM3
    Nodes=1G/           Solutions obtained by running our algorithm on high performance server (no time limit, but number of nodes explored is limited to 2^30)
      IDA-R/                Solutions files produced by IDA*-R
      IDA-U/                Solutions files produced by IDA*-U