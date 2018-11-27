static void vCAN_Send_u64(uint32_t __MSG_ID, uint8_t __MSG_LENGTH, uint64_t __Data, uint32_t __Timeout)
{
	hcan.pTxMsg = &myTxMessage;
	
	myTxMessage.StdId = __MSG_ID;
	myTxMessage.ExtId = __MSG_ID<<16;
	myTxMessage.DLC = __MSG_LENGTH;
	while 
	myTxMessage.Data[0] = (uint8_t)(__Data>>56);
	myTxMessage.Data[1] = (uint8_t)(__Data>>48);
	myTxMessage.Data[2] = (uint8_t)(__Data>>40);
	myTxMessage.Data[3] = (uint8_t)(__Data>>32);
	myTxMessage.Data[4] = (uint8_t)(__Data>>24);
	myTxMessage.Data[5] = (uint8_t)(__Data>>16);
	myTxMessage.Data[6] = (uint8_t)(__Data>>8);
	myTxMessage.Data[7] = (uint8_t)(__Data);
	myTxMessage.IDE = CAN_ID_EXT;
	myTxMessage.RTR = CAN_RTR_DATA;
	
	HAL_CAN_Transmit_IT(&hcan);
}
