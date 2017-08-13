#ifndef _TYPES_H_
#define _TYPES_H_

#include <stdint.h>

/* Max path length for each flow */
#define MAX_PATH_LENGTH 4

/* link and pair ids */
typedef uint16_t link_id_t;
typedef uint16_t pair_id_t;

/* bandwidth type variable */
typedef double bw_t;

struct link_t {
  link_id_t id;

  pair_id_t nactive_flows;
  pair_id_t nflows;
  bw_t capacity;
  bw_t used;

  struct flow_t **flows;
};

struct flow_t {
  pair_id_t id;

  uint8_t fixed;
  uint8_t nlinks;

  bw_t bw;
  bw_t demand;

  struct link_t *links[MAX_PATH_LENGTH];
};

/* Network representation */
struct network_t {
  link_id_t *routing;
  struct link_t *links;
  struct flow_t *flows;

  link_id_t num_links;
  pair_id_t num_flows;

  int fixed_flow_end;
  pair_id_t *flow_ids;

  int fixed_link_end;
  link_id_t *link_ids;
};

#endif